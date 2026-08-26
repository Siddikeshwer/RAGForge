import { useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [uploaded, setUploaded] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [asking, setAsking] = useState(false);
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    setUploading(true);
    setError("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        `${API_URL}/upload`,
        formData
      );

      setUploaded(true);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Failed to upload document."
      );
    } finally {
      setUploading(false);
    }
  };

  const handleAsk = async () => {
    if (!question.trim()) return;

    setAsking(true);
    setError("");
    setAnswer("");
    setSources([]);

    try {
      const response = await axios.post(
        `${API_URL}/ask`,
        {
          question: question
        }
      );

      setAnswer(response.data.answer);
      setSources(response.data.sources || []);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Failed to get an answer."
      );
    } finally {
      setAsking(false);
    }
  };

  return (
    <div className="app">

      {/* Sidebar */}
      <aside className="sidebar">

        <div className="logo">
          <div className="logo-mark">R</div>
          <span>RAGForge</span>
        </div>

        <div className="sidebar-section">
          <p className="section-title">DOCUMENTS</p>

          {uploaded && file ? (
            <div className="document-card">
              <div className="file-icon">PDF</div>

              <div className="file-info">
                <span>{file.name}</span>
                <small>Indexed</small>
              </div>

              <div className="status-dot"></div>
            </div>
          ) : (
            <div className="empty-documents">
              No documents yet
            </div>
          )}
        </div>

        <label className="upload-button">
          <input
            type="file"
            accept=".pdf,.docx,.txt"
            onChange={(e) => {
              setFile(e.target.files[0]);
              setUploaded(false);
            }}
          />

          <span>＋</span>
          Choose document
        </label>

        {file && !uploaded && (
          <button
            className="index-button"
            onClick={handleUpload}
            disabled={uploading}
          >
            {uploading ? "Indexing..." : "Index document"}
          </button>
        )}

        <div className="sidebar-bottom">
          <div className="pipeline">
            <span className="green-dot"></span>
            RAG pipeline online
          </div>

          <div className="pipeline-info">
            Hybrid retrieval · Reranking
          </div>
        </div>

      </aside>

      {/* Main */}
      <main className="main">

        <header className="topbar">
          <div>
            <h1>Ask your documents</h1>
            <p>
              Search your knowledge base with Hybrid RAG
            </p>
          </div>

          <div className="model-badge">
            <span></span>
            Ox Alpha
          </div>
        </header>

        <section className="content">

          {!answer && !asking && (
            <div className="welcome">
              <div className="welcome-icon">✦</div>

              <h2>What do you want to know?</h2>

              <p>
                Upload a document and ask questions.
                RAGForge retrieves the most relevant
                information before generating an answer.
              </p>
            </div>
          )}

          {asking && (
            <div className="loading-card">
              <div className="loader"></div>

              <div>
                <strong>Searching your documents</strong>
                <p>
                  Hybrid retrieval → reranking → Ox Alpha
                </p>
              </div>
            </div>
          )}

          {answer && !asking && (
            <div className="answer-section">

              <div className="answer-label">
                ANSWER
              </div>

              <div className="answer-card">
                <p>{answer}</p>
              </div>

              {sources.length > 0 && (
                <>
                  <div className="answer-label sources-title">
                    SOURCES
                  </div>

                  <div className="sources">

                    {sources.map((source, index) => {
                      const metadata =
                        source.metadata || {};

                      return (
                        <div
                          className="source-card"
                          key={index}
                        >
                          <div className="source-number">
                            {index + 1}
                          </div>

                          <div className="source-info">
                            <strong>
                              {metadata.source ||
                                "Unknown document"}
                            </strong>

                            <span>
                              {metadata.page
                                ? `Page ${metadata.page}`
                                : "Document"}
                            </span>
                          </div>

                          <div className="source-score">
                            {source.score.toFixed(2)}
                          </div>
                        </div>
                      );
                    })}

                  </div>
                </>
              )}

            </div>
          )}

          {error && (
            <div className="error">
              {error}
            </div>
          )}

          <div className="question-area">

            <textarea
              value={question}
              onChange={(e) =>
                setQuestion(e.target.value)
              }
              onKeyDown={(e) => {
                if (
                  e.key === "Enter" &&
                  !e.shiftKey
                ) {
                  e.preventDefault();
                  handleAsk();
                }
              }}
              placeholder="Ask anything about your documents..."
              rows="1"
            />

            <button
              className="ask-button"
              onClick={handleAsk}
              disabled={
                asking || !question.trim()
              }
            >
              {asking ? "..." : "Ask"}
            </button>

          </div>

          <div className="hint">
            Press Enter to ask · Shift + Enter for new line
          </div>

        </section>

      </main>

    </div>
  );
}

export default App;
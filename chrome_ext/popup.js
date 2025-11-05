/* global chrome */

"use strict";

/**
 * Retrieve the URL of the active tab within the current window.
 */
function getActiveTabUrl() {
  return new Promise((resolve) => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const [activeTab] = tabs;
      resolve(activeTab && activeTab.url ? activeTab.url : "");
    });
  });
}

/**
 * Placeholder function for invoking the backend phishing detector.
 * TODO: Integrate FastAPI prediction endpoint and handle response states.
 */
async function fetchPrediction(url) {
  return {
    url,
    prediction_label: "unknown",
    score: 0,
    message: "Placeholder response. API integration pending.",
  };
}

/**
 * Initialize popup interactions once DOM content is ready.
 */
function initPopup() {
  const scanButton = document.getElementById("scan-button");
  const resultContainer = document.getElementById("scan-result");

  if (!scanButton || !resultContainer) {
    return;
  }

  const updateResult = (text) => {
    resultContainer.textContent = text;
  };

  scanButton.addEventListener("click", async () => {
    updateResult("Scanning active tab URL...");

    const targetUrl = await getActiveTabUrl();
    if (!targetUrl) {
      updateResult("No active tab URL detected.");
      return;
    }

    updateResult(`Preparing prediction for: ${targetUrl}`);

    const response = await fetchPrediction(targetUrl);
    updateResult(
      `URL: ${response.url}\nLabel: ${response.prediction_label}\nScore: ${response.score}\n${response.message}`
    );
  });
}

document.addEventListener("DOMContentLoaded", initPopup);

// Cyber Safer - API Module

const API = {
  baseUrl: window.location.origin,

  // Get all scenarios grouped by category
  async getScenarios() {
    const res = await fetch(`${this.baseUrl}/api/scenarios`);
    return await res.json();
  },

  // Get a specific scenario
  async getScenario(scenarioId) {
    const res = await fetch(`${this.baseUrl}/api/scenario/${scenarioId}`);
    return await res.json();
  },

  // Start a scenario session
  async startScenario(scenarioId) {
    const res = await fetch(`${this.baseUrl}/api/scenario/${scenarioId}/start`, {
      method: 'POST'
    });
    return await res.json();
  },

  // Send a message (streaming)
  async sendMessage(message) {
    const res = await fetch(`${this.baseUrl}/api/chat/stream`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    return res.body.getReader();
  },

  // Complete the scenario and get results
  async completeScenario() {
    const res = await fetch(`${this.baseUrl}/api/scenario/complete`, {
      method: 'POST'
    });
    return await res.json();
  },

  // Exit scenario mode
  async exitScenario() {
    const res = await fetch(`${this.baseUrl}/api/scenario/exit`, {
      method: 'POST'
    });
    return await res.json();
  }
};

// PATCH FOR static/js/api.js or chat.html JavaScript
// Add this to handle counter updates from the backend

// In the message streaming handler, add this before displaying tokens:

function updateLastMessage(chunk) {
  const messagesDiv = document.getElementById('messages');
  let lastMsg = messagesDiv.lastElementChild;
  
  // Check for counter update marker
  if (chunk.startsWith('[COUNTER:') && chunk.includes(']')) {
    const match = chunk.match(/\[COUNTER:(\d+)\/(\d+)\]/);
    if (match) {
      const [_, current, total] = match;
      updateCounter(parseInt(current), parseInt(total));
      // Don't display the marker itself
      chunk = chunk.replace(/\[COUNTER:\d+\/\d+\]\n?/, '');
      if (!chunk) return; // Skip if only counter marker
    }
  }
  
  if (!lastMsg || !lastMsg.classList.contains('bot') || lastMsg.dataset.complete) {
    lastMsg = document.createElement('div');
    lastMsg.className = 'message bot';
    
    const label = document.createElement('span');
    label.className = 'label';
    label.textContent = `${adversaryName}:`;
    
    const content = document.createElement('div');
    content.className = 'content';
    content.textContent = '';
    
    lastMsg.appendChild(label);
    lastMsg.appendChild(content);
    messagesDiv.appendChild(lastMsg);
  }
  
  const content = lastMsg.querySelector('.content');
  content.textContent += chunk;
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function updateCounter(current, total) {
  // Update the counter display in the header
  const counterElement = document.getElementById('redFlagCounter');
  if (counterElement) {
    counterElement.textContent = `${current}/${total}`;
  }
  
  // Update progress bar if exists
  const progressBar = document.querySelector('.progress-bar');
  if (progressBar && total > 0) {
    const percentage = (current / total) * 100;
    progressBar.style.width = `${percentage}%`;
  }
  
  console.log(`🚩 Counter updated: ${current}/${total}`);
}

// Alternative: Poll for status updates
// Add this to periodically check the counter:

let statusCheckInterval = null;

function startStatusPolling() {
  if (statusCheckInterval) return;
  
  statusCheckInterval = setInterval(async () => {
    try {
      const response = await fetch('/api/scenario/status');
      const status = await response.json();
      
      if (status.active) {
        updateCounter(status.red_flags_found, status.red_flags_required);
      } else {
        stopStatusPolling();
      }
    } catch (error) {
      console.error('Status check failed:', error);
    }
  }, 2000); // Check every 2 seconds
}

function stopStatusPolling() {
  if (statusCheckInterval) {
    clearInterval(statusCheckInterval);
    statusCheckInterval = null;
  }
}

// Call startStatusPolling() when scenario begins
// Call stopStatusPolling() when scenario ends

async function loadDashboard() {
  const resp = await fetch('data/processed/dashboard.json');
  const data = await resp.json();

  // Top cards
  document.getElementById('totalInflow').textContent  = formatMoney(data.summary.total_inflow);
  document.getElementById('totalOutflow').textContent = formatMoney(data.summary.total_outflow);
  document.getElementById('net').textContent          = formatMoney(data.summary.total_inflow - data.summary.total_outflow);

  // Category chart
  const catCtx = document.getElementById('byCategory').getContext('2d');
  new Chart(catCtx, {
    type: 'bar',
    data: {
      labels: data.by_category.map(x => x.category),
      datasets: [{
        label: 'Amount',
        data: data.by_category.map(x => x.amount)
      }]
    },
    options: { responsive: true, scales: { y: { beginAtZero: true } } }
  });

  // Monthly trend
  const monCtx = document.getElementById('monthlyTrend').getContext('2d');
  new Chart(monCtx, {
    type: 'line',
    data: {
      labels: data.monthly.map(x => x.month),
      datasets: [{
        label: 'Net',
        data: data.monthly.map(x => x.net)
      }]
    },
    options: { responsive: true }
  });

  // Table
  const tbody = document.querySelector('#txTable tbody');
  tbody.innerHTML = '';
  data.latest.slice(0, 20).forEach(tx => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${tx.date}</td><td>${tx.category}</td><td>${formatMoney(tx.amount)}</td><td>${tx.counterparty||''}</td><td title="${tx.raw.replace(/"/g,'&quot;')}">view</td>`;
    tbody.appendChild(tr);
  });
}

function formatMoney(n) {
  if (n === null || n === undefined) return '—';
  return new Intl.NumberFormat(undefined, { style: 'currency', currency: 'RWF', maximumFractionDigits: 0 }).format(n);
}

loadDashboard().catch(console.error);

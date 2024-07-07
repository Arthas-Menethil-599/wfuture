const itemsPerPage = 5;
let currentPage = 1;

function renderOrganizations(companies) {
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedOrganizations = companies.slice(startIndex, endIndex);

  const organizationList = document.getElementById('organization-list');
  organizationList.innerHTML = '';

  paginatedOrganizations.forEach(company => {
    const orgElement = document.createElement('div');
    orgElement.className = 'organization';
    orgElement.innerHTML = `
      <h2>${company.name}</h2>
      <p style="overflow: hidden;">${company.description}</p>
    `;
    organizationList.appendChild(orgElement);
  });

  document.getElementById('page-info').textContent = `Page ${currentPage} of ${Math.ceil(companies.length / itemsPerPage)}`;
  document.getElementById('prev').disabled = currentPage === 1;
  document.getElementById('next').disabled = currentPage === Math.ceil(companies.length / itemsPerPage);
}

function changePage(direction, companies) {
  currentPage += direction;
  console.log(companies)
  renderOrganizations(companies);
}

document.addEventListener('DOMContentLoaded', () => {
  const companies = JSON.parse(document.getElementById('companies-data').textContent);
  renderOrganizations(companies);
});

// document.addEventListener('DOMContentLoaded', () => {
//     const searchInput = document.getElementById('search');
//     const locationSelect = document.getElementById('location');
//     const jobTypeSelect = document.getElementById('job-type');
//     const filterButton = document.getElementById('filter-button');
//     const jobListingsContainer = document.querySelector('.job-listings');
//     const prevPageButton = document.getElementById('prev-page');
//     const nextPageButton = document.getElementById('next-page');
//     const pageInfo = document.getElementById('page-info');

//     const jobs = [
//         { title: "Software Engineer", company: "Tech Corp", location: "New York", type: "Full Time" },
//         { title: "Project Manager", company: "Business Solutions", location: "San Francisco", type: "Part Time" },
//         { title: "Data Analyst", company: "Data Inc.", location: "Remote", type: "Contract" },
//         { title: "UX Designer", company: "Creative Agency", location: "New York", type: "Full Time" },
//         { title: "Marketing Specialist", company: "Marketing Pros", location: "San Francisco", type: "Full Time" },
//         { title: "Software Engineer 2", company: "Tech Corp", location: "New York", type: "Full Time" },
//         { title: "Project Manager 2", company: "Business Solutions", location: "San Francisco", type: "Part Time" },
//         { title: "Data Analyst 2", company: "Data Inc.", location: "Remote", type: "Contract" },
//         { title: "UX Designer 2", company: "Creative Agency", location: "New York", type: "Full Time" },
//         { title: "Marketing Specialist 2", company: "Marketing Pros", location: "San Francisco", type: "Full Time" },
//         // Add more job listings as needed
//     ];

//     let filteredJobs = jobs;
//     let currentPage = 1;
//     const jobsPerPage = 5;
//     const totalPages = Math.ceil(filteredJobs.length / jobsPerPage);

//     const renderJobs = () => {
//         jobListingsContainer.innerHTML = '';
//         const start = (currentPage - 1) * jobsPerPage;
//         const end = start + jobsPerPage;
//         const jobsToDisplay = filteredJobs.slice(start, end);

//         jobsToDisplay.forEach(job => {
//             const jobListing = document.createElement('div');
//             jobListing.classList.add('job-listing');
//             jobListing.innerHTML = `
//                 <h2>${job.title}</h2>
//                 <p>${job.company}</p>
//                 <p>${job.location}</p>
//                 <p>${job.type}</p>
//             `;
//             jobListingsContainer.appendChild(jobListing);
//         });

//         pageInfo.textContent = `Page ${currentPage} of ${totalPages}`;
//         prevPageButton.disabled = currentPage === 1;
//         nextPageButton.disabled = currentPage === totalPages;
//     };

//     const filterJobs = () => {
//         const searchQuery = searchInput.value.toLowerCase();
//         const locationFilter = locationSelect.value;
//         const jobTypeFilter = jobTypeSelect.value;

//         filteredJobs = jobs.filter(job => {
//             const matchesSearch = job.title.toLowerCase().includes(searchQuery) || job.company.toLowerCase().includes(searchQuery);
//             const matchesLocation = !locationFilter || job.location === locationFilter;
//             const matchesJobType = !jobTypeFilter || job.type === jobTypeFilter;
//             return matchesSearch && matchesLocation && matchesJobType;
//         });

//         currentPage = 1;
//         renderJobs();
//     };

//     filterButton.addEventListener('click', filterJobs);

//     prevPageButton.addEventListener('click', () => {
//         if (currentPage > 1) {
//             currentPage--;
//             renderJobs();
//         }
//     });

//     nextPageButton.addEventListener('click', () => {
//         if (currentPage < totalPages) {
//             currentPage++;
//             renderJobs();
//         }
//     });

//     filterJobs(); 
// });

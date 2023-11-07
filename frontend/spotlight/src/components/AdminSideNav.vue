<template>
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-dark sidebar collapse" style="">
      <div class="position-sticky pt-3">
        <h6 class="d-flex justify-content-between align-items-center ps-1 mt-4 mb-1">
          <a class="nav-link active" aria-current="page" href="#">Creator Requests</a>
        </h6>
        <ul class="nav flex-column mb-2">
          <li class="nav-item">
            <a class="nav-link" href="#">
              user 1
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              user 2
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              user 3
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              user 4
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              No new Requests
            </a>
          </li>
        </ul>
        <h6 class="d-flex justify-content-between align-items-center ps-1 mt-4 mb-1">
          <a class="nav-link active" aria-current="page" href="#">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" stroke="currentColor"
              stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home"
              aria-hidden="true">
              <path
                d="M20 2H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 5h-3v5.5c0 1.38-1.12 2.5-2.5 2.5S10 13.88 10 12.5s1.12-2.5 2.5-2.5c.57 0 1.08.19 1.5.51V5h4v2zM4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6z" />
            </svg>
            Genre Requests
            <a class="link-secondary" href="#" aria-label="Add a new report">
              <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none"
                stroke="var(--bp-khaki)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                class="feather feather-plus-circle" aria-hidden="true">
                <!-- <circle cx="12" cy="12" r="10"></circle> -->
                <line x1="12" y1="8" x2="12" y2="16"></line>
                <line x1="8" y1="12" x2="16" y2="12"></line>
              </svg>
            </a>
          </a>
        </h6>
        <ul class="nav flex-column mb-3">
          <li class="nav-item">
            <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
              <a class="nav-link" href="#">Genre 1</a>
            </h6>
          </li>
          <li class="nav-item">
            <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
              <a class="nav-link" href="#">Genre 2</a>
            </h6>
          </li>
          <li class="nav-item">
            <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
              <a class="nav-link" href="#">Genre 3</a>
            </h6>
          </li>
          <li class="nav-item">
            <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
              <a class="nav-link" href="#">Genre 4</a>
            </h6>
          </li>
          <li class="nav-item">
            <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
              <a class="nav-link" href="#">No new Requests</a>
            </h6>
          </li>
        </ul>
      </div>
    </nav>
  </template>
  <script>
  export default {
    name: 'AdminSideNav',
  }
  </script>
  <style>
  .sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 100;
    padding: 48px 0 0;
    box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
    overflow-x: hidden;
    overflow-y: auto;
    /* Hide scrollbar for IE, Edge and Firefox */
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  
  /* Hide scrollbar for Chrome, Safari and Opera */
  .sidebar::-webkit-scrollbar {
    display: none;
  }
  
  @media (max-width: 767.98px) {
    .sidebar {
      top: 5rem;
    }
  }
  
  .sidebar-sticky {
    position: relative;
    top: 0;
    height: calc(100vh - 48px);
    padding-top: .5rem;
    overflow-x: hidden;
    overflow-y: hidden;
  }
  
  .sidebar .nav-link {
    font-weight: 500;
    color: #fff;
  }
  
  .sidebar .nav-link .feather {
    margin-right: 4px;
    color: var(--bp-khaki);
  }
  
  .sidebar .nav-link.active {
    color: var(--bp-khaki);
  }
  
  .sidebar .nav-link:hover .feather,
  .sidebar .nav-link.active .feather {
    color: var(--bp-khaki);
  }
  
  .sidebar a:hover {
    color: var(--bp-khaki);
  }
  </style>
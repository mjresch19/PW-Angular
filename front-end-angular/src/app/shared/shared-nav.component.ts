import { Component } from '@angular/core';

@Component({
  selector: 'app-shared-nav',
  standalone: true,
  imports: [],
  template: `
    <nav>
      <div class="flex-container">
          <div id="sidebar" class="sidebar" aria-label="sidebar" aria-hidden="true">
            <div class="sidebar_content">
              <a href="localhost:4200/home">Home Page</a>
            </div>
            <div class="sidebar_content">
              <a href="localhost:4200/projects">Project Page</a>
            </div>
            <div class="sidebar_content">
              <a href="localhost:4200/piano">Piano Page</a>
            </div>
            <div class="sidebar_content">
              <a href="localhost:4200/resume">Resume</a>
            </div>
            <div class="sidebar_content">
              <a href="localhost:4200/chat">Chat</a>
            </div>
            <div class="sidebar_content">
            <a href="localhost:4200/login">Login</a>
            </div>
            <div class="sidebar_content">
              <a  target="_blank" href="https://www.linkedin.com/in/max-resch-22646219b/">LinkedIn</a>
            </div>
          </div>
            <h1>Welcome to Max's Website!<span style="font-size: 16px"><br>CSE 477 - Homework 3</span></h1>
          <!-- <button data-toggle-sidebar="sidebar"><img src="../static/main/images/clover-menu-bar.png" alt="clover-icon" loading="lazy" class="icon" id="icon-object"></img></button> -->
          <a href="localhost:4200/home">Home Page</a>
          <a href="localhost:4200/projects">Projects Page</a>
          <a href="localhost:4200/piano">Piano Page</a>
          <a href="localhost:4200/resume">Resume</a>
          <a href="localhost:4200/chat">Chat</a>
          <a href="localhost:4200/login">Login</a>
          <a target="_blank" href="https://www.linkedin.com/in/max-resch-22646219b/"><img src="../static/main/images/social-linkedin.png" alt="URL to LinkedIn Page" loading="lazy"></a>
      </div>
    </nav>
  `,
  styleUrl: './shared-nav.component.css'
})
export class BaseNavComponent {

}

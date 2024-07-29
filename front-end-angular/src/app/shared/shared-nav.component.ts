import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-shared-nav',
  standalone: true,
  imports: [RouterLink, RouterOutlet],
  template: `
    <nav>
      <div class="flex-container">
          <div id="sidebar" class="sidebar" aria-label="sidebar" aria-hidden="true">
            <div class="sidebar_content">
              <a routerLink="/home">Home Page</a>
            </div>
            <div class="sidebar_content">
              <a routerLink="/projects">Project Page</a>
            </div>
            <div class="sidebar_content">
              <a routerLink="/piano">Piano Page</a>
            </div>
            <div class="sidebar_content">
              <a routerLink="/resume">Resume</a>
            </div>
            <div class="sidebar_content">
              <a routerLink="/chat">Chat</a>
            </div>
            <div class="sidebar_content">
            <a routerLink="/login">Login</a>
            </div>
            <div class="sidebar_content">
              <a  target="_blank" href="https://www.linkedin.com/in/max-resch-22646219b/">LinkedIn</a>
            </div>
          </div>
            <h1>Welcome to Max's Website!<span style="font-size: 16px"><br>CSE 477 - Homework 3</span></h1>
          <!-- <button data-toggle-sidebar="sidebar"><img src="../assets/images/social-linkedin.png" alt="clover-icon" loading="lazy" class="icon" id="icon-object"></img></button> -->
          <a routerLink="/home">Home Page</a>
          <a routerLink="/projects">Projects Page</a>
          <a routerLink="/piano">Piano Page</a>
          <a routerLink="/resume">Resume</a>
          <a routerLink="/chat">Chat</a>
          <a routerLink="/login">Login</a>
          <a target="_blank" href="https://www.linkedin.com/in/max-resch-22646219b/"><img src="../assets/images/social-linkedin.png" alt="URL to LinkedIn Page" loading="lazy"></a>
      </div>
    </nav>
    <router-outlet></router-outlet>
  `,
  styleUrl: './shared-nav.component.css'
})
export class BaseNavComponent {

}

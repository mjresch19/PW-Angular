import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-shared-nav',
  standalone: true,
  imports: [RouterLink, RouterOutlet, NgOptimizedImage],
  template: `
    <nav>
      <ul class="link-group">
        <li><a routerLink="/home">Home</a></li>
        <li><a routerLink="/mytimeline">My Timeline</a></li>
        <li><a routerLink="/resume">Resume</a></li>
        <li><a routerLink="/login">Login</a></li>
        <li><a routerLink="/tester">Become a Tester *Coming Soon*</a></li>
        <li><a target="_blank" href="https://www.linkedin.com/in/max-resch-22646219b/"><img ngSrc="../assets/images/social-linkedin.png" alt="URL to LinkedIn Page" loading="lazy" width="40" height="40"></a></li>
      </ul>

    </nav>
    <router-outlet></router-outlet>
  `,
  styleUrl: './shared-nav.component.css'
})
export class BaseNavComponent {

}

/*
          <div id="sidebar" class="sidebar" aria-label="sidebar" aria-hidden="true">
            <div class="sidebar_content">
              <a routerLink="/home">Home</a>
            </div>
            <div class="sidebar_content">
              <a routerLink="/mytimeline">My Timeline</a>
            </div>
            <div class="sidebar_content">
              <a routerLink="/resume">Resume</a>
            </div>
            <div class="sidebar_content">
              <a routerLink="null">Become a Tester *Coming Soon*</a>
            </div>
            <div class="sidebar_content">
            <a routerLink="/login">Login</a>
            </div>
            <div class="sidebar_content">
              <a  target="_blank" href="https://www.linkedin.com/in/max-resch-22646219b/">LinkedIn</a>
            </div>
          </div>
            <!-- <h1>Welcome to Max's Website!</h1> -->
          <!-- <button data-toggle-sidebar="sidebar"><img src="../assets/images/social-linkedin.png" alt="clover-icon" loading="lazy" class="icon" id="icon-object"></img></button> -->


*/
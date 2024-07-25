import { Component } from '@angular/core';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-shared-header',
  standalone: true,
  imports: [NgOptimizedImage],
  template: `
    <header>
      <img ngSrc="../assets/images/summer-banner.jpg" alt="Summer Banner" loading="lazy" height="200" width="367">
    </header>
  `,
  styleUrl: './shared-header.component.css'
})
export class BaseHeaderComponent {

}
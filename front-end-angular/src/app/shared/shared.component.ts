import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterOutlet, NgOptimizedImage],
  templateUrl: './shared.component.html',
  styleUrls: [
    './shared-header.css',
    './shared-nav.css',
    './shared-main.css',
    './shared-footer.css',
  ],
})
export class BaseComponent {
  title = 'front-end-angular';
}

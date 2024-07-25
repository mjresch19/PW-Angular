import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { BaseComponent } from './shared/shared.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, BaseComponent],
  template: `
    <app-home></app-home>
  `,
  // templateUrl: './shared/shared.component.html',
  styleUrls: [
    './app.component.css'
  ],
})
export class AppComponent {
  title = 'front-end-angular';
}

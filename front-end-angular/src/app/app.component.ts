import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { HomeComponent } from './home/home.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, HomeComponent],
  template: `<app-home></app-home>`,
  styleUrls: [
    './app.component.css'
  ],
})
export class AppComponent {
  title = 'front-end-angular';
}

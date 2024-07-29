import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  template: `<router-outlet></router-outlet>`,
  styleUrls: [
    './app.component.css'
  ],
})
export class AppComponent {
  title = 'front-end-angular';
}

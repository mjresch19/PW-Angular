import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, HttpClientModule],
  template: `<router-outlet></router-outlet>`,
  styleUrls: [
    './app.component.css'
  ],
})
export class AppComponent {
  title = 'front-end-angular';
}

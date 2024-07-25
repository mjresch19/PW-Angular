import { Component } from '@angular/core';

@Component({
  selector: 'app-shared-footer',
  standalone: true,
  imports: [],
  template: `
    <footer>
        <p>© 2024 Max Jefffrey Resch</p>
    </footer>
  `,
  styleUrl: './shared-footer.component.css'
})
export class BaseFooterComponent {

}
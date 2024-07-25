import { Component } from '@angular/core';
import { BaseNavComponent } from '../shared/shared-nav.component';
import { BaseFooterComponent } from '../shared/shared-footer.component';

@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [BaseNavComponent, BaseFooterComponent],
  templateUrl: './resume.component.html',
  styleUrl: './resume.component.css'
})
export class ResumeComponent {

}

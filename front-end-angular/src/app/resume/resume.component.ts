import { Component } from '@angular/core';
import { BaseNavComponent } from '../shared/shared-nav.component';
import { BaseFooterComponent } from '../shared/shared-footer.component';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [BaseNavComponent, BaseFooterComponent, NgOptimizedImage],
  templateUrl: './resume.component.html',
  styleUrl: './resume.component.css'
})
export class ResumeComponent {

}

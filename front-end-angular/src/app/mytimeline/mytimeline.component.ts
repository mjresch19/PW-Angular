import { Component } from '@angular/core';
import { BaseNavComponent } from '../shared/shared-nav.component';
import { BaseFooterComponent } from '../shared/shared-footer.component';

@Component({
  selector: 'app-mytimeline',
  standalone: true,
  imports: [BaseNavComponent, BaseFooterComponent],
  templateUrl: './mytimeline.component.html',
  styleUrl: './mytimeline.component.css'
})
export class MyTimelineComponent {

}

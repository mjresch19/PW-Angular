import { Component } from '@angular/core';
import { BaseHeaderComponent } from '../shared/shared-header.component';
import { BaseNavComponent } from '../shared/shared-nav.component';
import { BaseMainComponent } from '../shared/shared-main.component';
import { BaseFooterComponent } from '../shared/shared-footer.component';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [BaseHeaderComponent, BaseNavComponent, BaseMainComponent, BaseFooterComponent, RouterLink, RouterOutlet],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}

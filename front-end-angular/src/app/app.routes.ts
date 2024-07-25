import { Routes } from '@angular/router';
import { BaseComponent } from './shared/shared.component';
import { AppComponent } from './app.component';

export const routes: Routes = [
    //We will use the home page as the root of the application for now
    {
        path: '',
        title: 'App Home Page',
        component: AppComponent,
    },
    {
        path: 'home',
        title: 'App Home Page',
        component: BaseComponent,
    },
];

import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AppComponent } from './app.component';

export const routes: Routes = [
    //We will use the home page as the root of the application for now
    {
        path: '',
        title: 'App Home Page',
        component: HomeComponent,
    },
    {
        path: 'home',
        title: 'App Home Page',
        component: HomeComponent,
    },
];

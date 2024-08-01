import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { MyTimelineComponent } from './mytimeline/mytimeline.component';
import { ResumeComponent } from './resume/resume.component';
import { LoginComponent } from './login/login.component';

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
    {
        path: 'mytimeline',
        title: 'My Timeline Page',
        component: MyTimelineComponent,
    },
    {
        path: 'resume',
        title: 'Resume Page',
        component: ResumeComponent,
    },
    {
        path: 'login',
        title: 'Login Page',
        component: LoginComponent,
    }
];

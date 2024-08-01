import { Component } from '@angular/core';
import { BaseNavComponent } from '../shared/shared-nav.component';
import { BaseFooterComponent } from '../shared/shared-footer.component';
import { RouterLink, RouterOutlet } from '@angular/router';
import { FormControl, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from '../../../models/User';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, BaseNavComponent, BaseFooterComponent, RouterLink, RouterOutlet],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

    constructor(private http: HttpClient) {

    }

    loginForm = new FormGroup({
      email: new FormControl('', [Validators.required, Validators.email]),
      password: new FormControl('', Validators.required),
    });
  
    login() {
        // Call API with username and password
        if (this.loginForm.invalid) return;

        const formValues = this.loginForm.value;

        const user:User = {
        email: formValues.email ?? '',
        password: formValues.password ?? '',
        };

        const headers = new HttpHeaders({
        "Access-Control-Allow-Origin": ["POST"],
        "Content-Type": "application/json",
        "Accept": "application/json"
        });

        this.http.post('http://localhost:8080/processlogin', user, {headers}).subscribe(
        response => {
            alert('Login successful');
            },
            error => {
            alert('Login failed');
            }
        );
        

        alert('Calling backend to login');
    }

  }

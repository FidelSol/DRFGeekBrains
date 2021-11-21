import React from 'react';
import './App.css';
import UserList from './components/Users.js';
import ProjectList from './components/Projects.js';
import ProjectFilteredList from './components/Project.js'
import ToDoList from './components/ToDos.js';
import axios from 'axios';
import {BrowserRouter, Route, Link, Routes} from 'react-router-dom'
import LoginForm from './components/Auth.js'
import UserLogout from './components/Exit.js'
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}



class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': [],
           'token': ''
       }
   }

   get_headers() {
        let headers = {
          'Content-Type': 'application/json'
        }
      if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


   componentDidMount() {
            const headers = this.get_headers()

            axios.get('http://127.0.0.1:8000/api/v1/users', {headers})
            .then(response => {
               const authors = response.data
                   this.setState(
                   {
                       'authors': authors
                   }
               )
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/v1/presentprojects', {headers})
            .then(response => {
               const projects = response.data
                   this.setState(
                   {
                       'projects': projects
                   }
               )
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/v1/presenttodos', {headers})
            .then(response => {
               const todos = response.data
                   this.setState(
                   {
                       'todos': todos
                   }
               )
            }).catch(error => console.log(error))

            this.get_token_from_storage()
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
      }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }



    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
      }

   render () {
       return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todos'>ToDos</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                            <Route path='/' element={() => <UserList items={this.state.users} />}  />
                            <Route path='/projects' element={() => <ProjectList items={this.state.projects} />} />
                            <Route path='/todos' element={() => <ToDoList items={this.state.todos} />} />
                            <Route path='/project/:id'>
                                <ProjectFilteredList items={this.state.projects} />
                            </Route>
                            <Route path='/login' element={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                            <Route component={NotFound404} />
                    </Routes>
                </BrowserRouter>
            </div>


       )
   }
}


export default App;

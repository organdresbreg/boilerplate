import { Router, Route } from 'preact-router'
import { Home } from './pages/Home'
import { About } from './pages/About'
import { Header } from './components/Header'

export function App() {
  return (
    <div class="app">
      <Header />
      <Router>
        <Route path="/" component={Home} />
        <Route path="/about" component={About} />
      </Router>
    </div>
  )
}

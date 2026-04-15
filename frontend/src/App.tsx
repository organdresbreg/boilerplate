import { Router, Route } from 'preact-router'
import { Home } from './pages/Home'
import { About } from './pages/About'
import { Header } from './components/Header'
import { ProtectedRoute } from './components/ProtectedRoute'
import { AuthGuard } from './components/AuthGuard'
import { ErrorBanner } from './components/ErrorBanner'

export function App() {
  return (
    <div class="app">
      <AuthGuard />
      <ErrorBanner />
      <Header />
      <Router>
        <Route path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/dashboard">
          <ProtectedRoute>
            <div class="p-4">
              <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
              <p>Protected content for authenticated users only.</p>
            </div>
          </ProtectedRoute>
        </Route>
      </Router>
    </div>
  )
}

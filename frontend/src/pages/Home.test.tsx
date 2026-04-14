import { render, screen } from '@testing-library/preact'
import { describe, it, expect } from 'vitest'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { Home } from '../pages/Home'

const createWrapper = () => {
  const client = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
    },
  })
  
  return ({ children }: { children: any }) => (
    <QueryClientProvider client={client}>{children}</QueryClientProvider>
  )
}

describe('Home', () => {
  it('renders welcome message', () => {
    render(<Home />, { wrapper: createWrapper() })
    expect(screen.getByText(/Welcome to Modern Full-Stack 2026/i)).toBeInTheDocument()
  })
})

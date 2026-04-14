import { render, screen, waitFor } from '@testing-library/preact'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { Home } from '../pages/Home'

global.fetch = vi.fn()

beforeEach(() => {
  vi.clearAllMocks()
})

describe('Home', () => {
  it('renders welcome message', async () => {
    vi.mocked(global.fetch).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ status: 'ok', version: '2.0.0', year: 2026 }),
    } as Response)

    render(<Home />)
    
    // El mensaje de bienvenida está presente desde el inicio
    await waitFor(() => {
      expect(screen.getByText(/Welcome to Modern Full-Stack 2026/i)).toBeInTheDocument()
    })
    
    await waitFor(() => {
      expect(screen.getByText(/API Status/i)).toBeInTheDocument()
    })
  })

  it('shows loading state initially', () => {
    vi.mocked(global.fetch).mockImplementationOnce(
      () => new Promise(() => {}) // Never resolves
    )

    render(<Home />)
    expect(screen.getByText('Loading...')).toBeInTheDocument()
  })

  it('shows error state on failure', async () => {
    vi.mocked(global.fetch).mockRejectedValueOnce(new Error('Network error'))

    render(<Home />)
    
    // El error se muestra después de que el hook maneja el rechazo
    await waitFor(() => {
      const errorElement = screen.queryByText('Error loading health check')
      expect(errorElement).toBeInTheDocument()
    }, { timeout: 1000 })
  })
})

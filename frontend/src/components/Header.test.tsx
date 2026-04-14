import { render, screen } from '@testing-library/preact'
import { describe, it, expect } from 'vitest'
import { Header } from '../components/Header'

describe('Header', () => {
  it('renders header with title', () => {
    render(<Header />)
    expect(screen.getByText(/🚀 Modern Full-Stack 2026/i)).toBeInTheDocument()
  })
})

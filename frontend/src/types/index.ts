export interface ApiResponse<T = unknown> {
  data?: T
  error?: string
  status: 'success' | 'error'
}

export interface User {
  id: number
  email: string
  full_name: string | null
  is_active: boolean
  created_at: string
  updated_at: string | null
}

export interface HealthCheck {
  status: string
  version: string
  year: number
}

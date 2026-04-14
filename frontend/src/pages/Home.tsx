import { useQuery } from '../hooks/useQuery'

export function Home() {
  const { data, isLoading, error } = useQuery<{ status: string; version: string; year: number }>(
    ['health'],
    async () => {
      const res = await fetch('/api/health')
      if (!res.ok) throw new Error('Network response was not ok')
      return res.json()
    }
  )

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error loading health check</div>

  return (
    <div class="home">
      <h2>Welcome to Modern Full-Stack 2026</h2>
      <p>Built with FastAPI + Preact + Vite</p>
      
      {data && (
        <div class="status">
          <h3>API Status</h3>
          <p>Status: {data.status}</p>
          <p>Version: {data.version}</p>
          <p>Year: {data.year}</p>
        </div>
      )}
    </div>
  )
}

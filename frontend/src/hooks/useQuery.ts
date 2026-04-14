import { useState, useEffect } from 'preact/hooks'

type QueryResult<T> = {
  data: T | null
  isLoading: boolean
  error: Error | null
}

export function useQuery<T>(
  queryKey: string[],
  queryFn: () => Promise<T>
): QueryResult<T> {
  const [data, setData] = useState<T | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    let mounted = true

    const fetchData = async () => {
      try {
        setIsLoading(true)
        const result = await queryFn()
        if (mounted) {
          setData(result)
          setError(null)
        }
      } catch (err) {
        if (mounted) {
          setError(err instanceof Error ? err : new Error('Unknown error'))
        }
      } finally {
        if (mounted) {
          setIsLoading(false)
        }
      }
    }

    fetchData()

    return () => {
      mounted = false
    }
  }, [queryKey.join(',')])

  return { data, isLoading, error }
}

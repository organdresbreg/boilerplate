import { useEffect, useState } from 'preact/hooks';
import { useAuthStore } from '../store/auth';
import { route } from 'preact-router';

interface ProtectedRouteProps {
  children: any;
}

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { user, loading, checkAuth } = useAuthStore();
  const [isChecking, setIsChecking] = useState(true);

  useEffect(() => {
    const verifyAuth = async () => {
      try {
        await checkAuth();
      } catch (error) {
        console.error('Auth verification failed:', error);
      } finally {
        setIsChecking(false);
      }
    };

    if (loading) {
      verifyAuth();
    } else {
      setIsChecking(false);
    }
  }, [loading, checkAuth]);

  // Show loading state while checking authentication
  if (isChecking || (loading && !user)) {
    return (
      <div class="flex items-center justify-center min-h-screen">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  // Redirect to login if not authenticated
  if (!user) {
    // Use setTimeout to prevent flash of protected content
    setTimeout(() => route('/login', true), 0);
    return null;
  }

  // Render children if authenticated
  return children;
}

import { useEffect } from 'preact/hooks';
import { useAuthStore } from '../store/auth';
import { route } from 'preact-router';

export function AuthGuard() {
  const { error, clearError } = useAuthStore();

  useEffect(() => {
    if (error) {
      // Handle specific error types
      if (error.includes('401') || error.includes('403')) {
        // Unauthorized or Forbidden - redirect to login
        setTimeout(() => {
          clearError();
          route('/login', true);
        }, 100);
      } else if (error.includes('Network Error') || error.includes('500')) {
        // Server or network error - show notification
        console.error('Global Error:', error);
        // In a real app, you would show a toast/notification here
        setTimeout(() => clearError(), 5000);
      }
    }
  }, [error, clearError]);

  return null;
}

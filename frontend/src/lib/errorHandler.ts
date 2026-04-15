import { signal } from '@preact/signals';

export const errorSignal = signal<string | null>(null);

export function showError(message: string) {
  errorSignal.value = message;
  
  // Auto-clear after 5 seconds for non-critical errors
  setTimeout(() => {
    if (errorSignal.value === message) {
      errorSignal.value = null;
    }
  }, 5000);
}

export function clearError() {
  errorSignal.value = null;
}

import numpy as np

class FCM:
    def __init__(
        self, n_clusters=10, max_iter=150, m=2, error=1e-5, random_state=42
    ):
        assert m > 1
        self.u, self.centers = None, None
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.m = m
        self.error = error
        self.list_of_error = []
        self.rng = np.random.default_rng(random_state)

    def fit(self, X, u=None):

        self.n_samples = X.shape[0]
        self.u = self.rng.uniform(size=(self.n_samples, self.n_clusters))
        self.u = self.u / np.tile(self.u.sum(axis=1)
                                  [np.newaxis].T, self.n_clusters)

        if (u is not None):
            self.u = u.copy()

        self.initial_u = self.u.copy()

        for iteration in range(self.max_iter):
            u_old = self.u.copy()
            self.centers = FCM._next_centers(X, self.u, self.m)
            self.u = self.__predict(X)
            err = np.linalg.norm(self.u - u_old)
            self.list_of_error.append({'iterasi': iteration+1, 'error': err})
            # Stopping rule
            if np.linalg.norm(self.u - u_old) < self.error:
                break

    def __predict(self, X):

        temp = FCM._dist(X, self.centers) ** float(2 / (self.m - 1))
        denominator_ = temp.reshape(
            (X.shape[0], 1, -1)).repeat(temp.shape[-1], axis=1)
        denominator_ = temp[:, :, np.newaxis] / denominator_
        return 1 / denominator_.sum(2)

    def predict(self, X):

        X = np.expand_dims(X, axis=0) if len(X.shape) == 1 else X
        return self.__predict(X).argmax(axis=-1)

    @staticmethod
    def _dist(A, B):
        """Compute the euclidean distance two matrices"""
        return np.sqrt(np.einsum("ijk->ij", (A[:, None, :] - B) ** 2))

    @staticmethod
    def _next_centers(X, u, m):
        """Update cluster centers"""
        um = u ** m
        return (X.T @ um / np.sum(um, axis=0)).T

    # partition coefficient (Equation 12a of https://doi.org/10.1016/0098-3004(84)90020-7)
    @property
    def partition_coefficient(self):
        if hasattr(self, "u"):
            return np.sum(self.u ** 2) / self.n_samples
        else:
            raise ReferenceError(
                "You need to train the model first. You can use `.fit()` "
                "method to this."
            )

    @property
    def partition_entropy_coefficient(self):
        if hasattr(self, "u"):
            return -np.sum(self.u * np.log2(self.u)) / self.n_samples
        else:
            raise ReferenceError(
                "You need to train the model first. You can use `.fit()` "
                "method to this."
            )





class FCMNative:
    def __init__(
        self, n_clusters=10, max_iter=150, m=2, error=1e-5, random_state=42
    ):
        assert m > 1
        self.u, self.centers = None, None
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.m = m
        self.error = error
        self.list_of_error = []
        self.rng = np.random.default_rng(random_state)

    def fit(self, X, u=None):

        self.n_samples = X.shape[0]
        self.u = self.rng.uniform(size=(self.n_samples, self.n_clusters))
        self.u = self.u / np.tile(self.u.sum(axis=1)
                                  [np.newaxis].T, self.n_clusters)

        if (u is not None):
            self.u = u.copy()

        self.initial_u = self.u.copy()

        for iteration in range(self.max_iter):
            u_old = self.u.copy()
            self.centers = FCM._next_centers(X, self.u, self.m)
            self.u = self.__predict(X)
            err = np.linalg.norm(self.u - u_old)
            self.list_of_error.append({'iterasi': iteration+1, 'error': err})
            # Stopping rule
            if np.linalg.norm(self.u - u_old) < self.error:
                break

    def __predict(self, X):

        temp = FCM._dist(X, self.centers) ** float(2 / (self.m - 1))
        denominator_ = temp.reshape(
            (X.shape[0], 1, -1)).repeat(temp.shape[-1], axis=1)
        denominator_ = temp[:, :, np.newaxis] / denominator_
        return 1 / denominator_.sum(2)

    def predict(self, X):

        X = np.expand_dims(X, axis=0) if len(X.shape) == 1 else X
        return self.__predict(X).argmax(axis=-1)

    @staticmethod
    def _dist(A, B):
        """Compute the euclidean distance two matrices"""
        return np.sqrt(np.einsum("ijk->ij", (A[:, None, :] - B) ** 2))

    @staticmethod
    def _next_centers(X, u, m):
        """Update cluster centers"""
        um = u ** m
        return (X.T @ um / np.sum(um, axis=0)).T

    # partition coefficient (Equation 12a of https://doi.org/10.1016/0098-3004(84)90020-7)
    @property
    def partition_coefficient(self):
        if hasattr(self, "u"):
            return np.sum(self.u ** 2) / self.n_samples
        else:
            raise ReferenceError(
                "You need to train the model first. You can use `.fit()` "
                "method to this."
            )

    @property
    def partition_entropy_coefficient(self):
        if hasattr(self, "u"):
            return -np.sum(self.u * np.log2(self.u)) / self.n_samples
        else:
            raise ReferenceError(
                "You need to train the model first. You can use `.fit()` "
                "method to this."
            )


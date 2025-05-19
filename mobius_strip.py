import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

class MobiusStrip:
    def __init__(self, R=1, w=0.3, n=100):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._compute_points()

    def _compute_points(self):
        u = self.U
        v = self.V
        R = self.R
        x = (R + v * np.cos(u / 2)) * np.cos(u)
        y = (R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def surface_area(self):
        def partial_u(u, v):
            dx_du = - (self.R + v * np.cos(u / 2)) * np.sin(u) - v * 0.5 * np.sin(u / 2) * np.cos(u)
            dy_du = (self.R + v * np.cos(u / 2)) * np.cos(u) - v * 0.5 * np.sin(u / 2) * np.sin(u)
            dz_du = v * 0.5 * np.cos(u / 2)
            return np.array([dx_du, dy_du, dz_du])

        def partial_v(u, v):
            dx_dv = np.cos(u / 2) * np.cos(u)
            dy_dv = np.cos(u / 2) * np.sin(u)
            dz_dv = np.sin(u / 2)
            return np.array([dx_dv, dy_dv, dz_dv])

        def integrand(v, u):
            du = partial_u(u, v)
            dv = partial_v(u, v)
            cross = np.cross(du, dv)
            return np.linalg.norm(cross)

        area, _ = dblquad(integrand, 0, 2 * np.pi, lambda u: -self.w / 2, lambda u: self.w / 2)
        return area

    def edge_length(self):
        def edge_curve(v_fixed):
            u_vals = np.linspace(0, 2 * np.pi, self.n)
            x = (self.R + v_fixed * np.cos(u_vals / 2)) * np.cos(u_vals)
            y = (self.R + v_fixed * np.cos(u_vals / 2)) * np.sin(u_vals)
            z = v_fixed * np.sin(u_vals / 2)
            return np.vstack((x, y, z)).T

        def curve_length(points):
            diffs = np.diff(points, axis=0)
            seg_lengths = np.linalg.norm(diffs, axis=1)
            return np.sum(seg_lengths)

        edge1 = edge_curve(self.w / 2)
        edge2 = edge_curve(-self.w / 2)
        return curve_length(edge1) + curve_length(edge2)

    def plot(self):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='k', alpha=0.8)
        ax.set_title("Möbius Strip")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

if __name__ == "__main__":
    mobius = MobiusStrip(R=1, w=0.3, n=200)
    print(f"Approximated Surface Area: {mobius.surface_area():.5f}")
    print(f"Approximated Edge Length: {mobius.edge_length():.5f}")
    mobius.plot()

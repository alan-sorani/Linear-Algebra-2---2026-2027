"""Draw two 2D parallelograms spanned by vectors from the origin.

Run with: python parallelepiped_volumes.py
Requires: matplotlib, numpy
"""

import matplotlib.pyplot as plt
import numpy as np


V1 = np.array([2.0, 0.0])
V2 = np.array([0.0, 1.0])


def draw_figure(second_edge, second_label, filename):
    """Shade the parallelogram and draw both vectors from the origin."""
    origin = np.zeros(2)
    corners = np.array([origin, V1, V1 + second_edge, second_edge])
    same_edge = np.allclose(second_edge, V1)
    x_max = (V1[0] if same_edge else (V1 + second_edge)[0]) + 0.5
    fig, ax = plt.subplots(figsize=(max(8, x_max * 1.6), 4.5))
    if not same_edge:
        ax.fill(corners[:, 0], corners[:, 1], color="#f5b544", alpha=0.5,
                edgecolor="#a45a00", linewidth=2.5, zorder=2)

    # When the vectors coincide, one arrow represents both of them.
    vectors = ((V1, second_label, "#c73535"),) if same_edge else (
        (V1, r"$(2,0)$", "#c73535"),
        (second_edge, second_label, "#187e6b"),
    )
    for edge, label, color in vectors:
        ax.annotate("", xy=edge, xytext=origin,
                    arrowprops=dict(arrowstyle="-|>", color=color,
                                    linewidth=3, mutation_scale=22),
                    zorder=4)
        label_x = edge[0] - 0.06 if edge[0] > 1 else edge[0] + 0.07
        label_align = "right" if edge[0] > 1 else "left"
        ax.text(label_x, edge[1] + 0.07, label, ha=label_align,
                color=color, fontsize=18, fontweight="bold", zorder=5)

    ax.scatter(0, 0, color="black", s=45, zorder=6)
    ax.set(xlim=(-0.25, x_max), ylim=(-0.25, 1.4),
           xlabel="x", ylabel="y")
    ax.set_xticks(np.arange(0, x_max, 0.5))
    ax.set_yticks(np.arange(0, 1.51, 0.5))
    ax.tick_params(labelsize=13)
    ax.xaxis.label.set_size(16)
    ax.yaxis.label.set_size(16)
    ax.set_aspect("equal")
    ax.set_axisbelow(True)
    ax.grid(True, color="#c4c4c4", linewidth=0.8)
    ax.axhline(0, color="#555555", linewidth=1)
    ax.axvline(0, color="#555555", linewidth=1)
    fig.tight_layout()
    fig.savefig(filename, dpi=220)
    plt.close(fig)


if __name__ == "__main__":
    draw_figure(V2, r"$(0,1)$", "parallelogram_v1_v2.png")
    draw_figure(V2 + 0.5 * V1, r"$(1,1)$",
                "parallelogram_v1_v2_plus_half_v1.png")
    draw_figure(V1, r"$(2,0)$", "parallelogram_v1_v1.png")

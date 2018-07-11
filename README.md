# orthogonalization

## Gram-Schmidt Orthogonalization

Orthonormal matrices are nice. They...

Gram-Schmidt is a simple algorithm for taking a non-orthonormal matrix ($A$) consisting of linear independent columns and creates an orthonormal version of the matrix ($Q$). The algorithm can be described as follows. Assume that we have an Array $A$ consisting of columns $\mathbf{a_i}$.

\begin{equation}
A=\begin{bmatrix}
\begin{array}{cccc{\qquad}1}
\mathbf{a_1} & \mathbf{a_2} & \cdots & \mathbf{a_n}
\end{array}
\end{bmatrix}
\end{equation}


1. Pick a column (vector); anyone will do so we might as well pick $\mathbf{a_{i=0}}$.
1. Create a unit vector version of $\mathbf{a_i}$ ($\mathbf{q_i}$) by dividing $\mathbf{a_i}$ by its norm ($\frac{\mathbf{a_i}}{||\mathbf{a_i}||}$)
2. Subtract $\mathbf{q_i}$ from all subsequent vectors $\mathbf{q_{j>i}}$
\begin{equation}
\mathbf{a_{j_i}^\prime} = \mathbf{a_j} - (\mathbf{q_i}^T \mathbf{a_j}) \mathbf{q_i}
\end{equation}
3. Increment $i$ and repeat.



Thus for any column $j$ we subtract the projection of all columns $i$ ($i < j$), the final process can be expressed as

\begin{eqnarray}
\mathbf{a_j^\prime} = \mathbf{a_j} - \sum_{i=1}^{j-1}(\mathbf{q_i}^T \mathbf{a_j}) \mathbf{q_i}\\
\mathbf{q_j} = \frac{\mathbf{a_j^\prime}}{||\mathbf{a_j^\prime}||}
\end{eqnarray}
    

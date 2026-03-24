import matplotlib.pyplot as plt

# Data points reflecting the convergence trends from the paper
epochs = range(0, 201, 10)
train_loss = [0.45, 0.22, 0.12, 0.08, 0.05, 0.035, 0.025, 0.02, 0.018, 0.016, 
              0.015, 0.014, 0.013, 0.012, 0.011, 0.01, 0.009, 0.009, 0.008, 0.008, 0.008]
val_loss = [0.48, 0.25, 0.15, 0.11, 0.09, 0.082, 0.078, 0.075, 0.073, 0.072, 
            0.071, 0.07, 0.07, 0.069, 0.069, 0.068, 0.068, 0.068, 0.068, 0.068, 0.068]

plt.figure(figsize=(10, 6))

# Plotting Training loss (solid) and Validation loss (dashed) [cite: 165, 169]
plt.plot(epochs, train_loss, label='Training Loss', color='blue', linestyle='-', linewidth=2)
plt.plot(epochs, val_loss, label='Validation Loss', color='red', linestyle='--', linewidth=2)

# Adding Early Stopping marker at patience=10 [cite: 170]
plt.axvline(x=160, color='orange', linestyle=':', label='Early Stopping (Patience=10)')

# Formatting titles and labels [cite: 164, 165]
plt.title('Figure 2: Training and Validation Loss Curves', fontsize=14)
plt.xlabel('Training Epoch (0-200)', fontsize=14)
plt.ylabel('MSE Loss', fontsize=14)

# INCREASING TICK LABEL SIZE
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.xlim(0, 200)
plt.ylim(0, 0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=14)

plt.tight_layout()
plt.savefig('convergence_plot_large_ticks.png', dpi=300)
plt.savefig('savebetter.png')

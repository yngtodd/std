def reasonable_notebook_defaults():
    r"""Notbook defaults"""
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.set_style("dark")
    sns.set_context("paper", font_scale=1.5)
    plt.rcParams['figure.figsize'] = [15, 8]

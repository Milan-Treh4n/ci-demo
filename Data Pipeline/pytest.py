import os
import pandas as pd
import numpy as np
import pytest
import fit

def test_csv_saved(tmp_path):
    file = tmp_path / "data.csv"
    fit.save_csv(file)
    assert file.exists()

def test_plot_saved(tmp_path):
    file = tmp_path / "data.csv"
    fit.save_csv(file)
    plot_file = tmp_path / "plot.png"
    fit.save_plot(file, plot_file)
    assert plot_file.exists()

def test_csv_numeric(tmp_path):
    file = tmp_path / "data.csv"
    fit.save_csv(file)
    df = fit.load_data(file)
    assert pd.api.types.is_numeric_dtype(df["x"])
    assert pd.api.types.is_numeric_dtype(df["y"])

def test_fit_line(tmp_path):
    file = tmp_path / "data.csv"
    fit.save_csv(file)
    df = fit.load_data(file)
    slope, intercept = fit.fit_line(df)
    assert np.isclose(slope, 3, atol=0.3)
    assert np.isclose(intercept, 5, atol=0.5)

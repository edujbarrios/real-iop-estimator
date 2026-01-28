# Real IOP Estimator

Open source intraocular pressure estimation software from multiple [iCare tonometer](https://www.icare-world.com) measurements.

---

## About

[iCare tonometers](https://www.icare-world.com) measure intraocular pressure through multiple rapid impacts on the cornea and display an averaged value. However, **these averaged readings vary significantly between measurement sessions** due to:

- Individual corneal biomechanical properties
- Corneal thickness and hydration state
- Measurement angle and positioning
- Patient-specific ocular characteristics
- Post-surgical corneal changes

#### **The problem:**
Even when taking multiple measurements across different sessions, **each session might produce a different average**. This variability can mask the true intraocular pressure, especially in patients with corneal pathology, post-surgical eyes, or glaucoma.

#### **The solution:** 
This software processes multiple session averages (the values displayed by the iCare device across different measurement occasions, not the single messurements in one session) and applies robust statistical methods to estimate a more reliable IOP value that better reflects true intraocular pressure.

**Clinical applications:**
- Glaucoma monitoring and progression tracking
- Post-surgical eyes (trabeculectomy, tube shunts, corneal procedures)
- Hypotony detection and management
- Corneal pathology (keratoconus, ectasia, irregular corneas)

---

## Quick Start

The usage has been simplified for ease of use, however note that this software assumes that you have **basic knowledge of Python** and have it installed on your system.

```bash
git clone https://github.com/edujbarrios/real-iop-estimator.git
cd real-iop-estimator
pip install -r requirements.txt
python app.py
```

Follow the interactive instructions.

> [!NOTE]  
> **In new versions, the idea is to distribute an .exe or similar file for easy execution without Python setup, as a standalone app.**

If you are a software developer, please refer to the [Developer Documentation](./dev_docs/00-index.mdx) for detailed implementation insights.

## Methods

### Primary Method

**Safe IOP (Trimmed Mean):**
$$IOP_{safe} = \frac{\sum IOP_i - IOP_{min} - IOP_{max}}{n - 2}$$

Eliminates the two most extreme outliers while preserving central tendency. Most reliable for clinical decisions, particularly in post-surgical cases and glaucoma monitoring where corneal biomechanical variability can mask true pressure values.

---

### Advanced Robust Methods

**Trimean IOP (Tukey's Method):**
$$IOP_{trimean} = \frac{Q_1 + 2 \cdot \text{Median} + Q_3}{4}$$

Combines quartiles and median with weighted average. Highly resistant to corneal biomechanical outliers from post-surgical eyes, keratoconus, and ectasia. The quartile-based approach accounts for measurement distribution shape affected by variable corneal properties.

**Interquartile Mean (IQM):**
$$IOP_{IQM} = \frac{2}{n} \sum_{i=\lfloor n/4 \rfloor}^{\lceil 3n/4 \rceil} IOP_{(i)}$$

Averages the middle 50% of data, eliminating both upper and lower quartiles. Superior for irregular corneal surfaces where extreme measurements arise from localized biomechanical variations or measurement angle inconsistencies. Optimal for corneal pathology patients.

**Winsorized Mean:**
$$IOP_{wins} = \frac{1}{n}\left(IOP_{(2)} + \sum_{i=2}^{n-1} IOP_{(i)} + IOP_{(n-1)}\right)$$

Replaces extremes with adjacent values instead of removing them. Maintains sample size (critical when n < 10), important for longitudinal monitoring with limited measurements. Reduces tear film artifact impact and smooths corneal hydration state variations across measurement sessions.

**Weighted Mean (Consistency-Based):**
$$IOP_{weighted} = \frac{\sum_{i=1}^{n} w_i \cdot IOP_i}{\sum_{i=1}^{n} w_i}, \quad w_i = \frac{1}{1 + |IOP_i - \text{Median}|}$$

Soft outlier rejection without hard cutoffs. Automatically downweights measurements affected by variable corneal hydration or diurnal IOP fluctuations while preserving all measurement information. Adaptive to measurement consistency patterns.

---

### Standard Methods

**Possible IOP (Median):**
$$IOP_{possible} = \text{median}(IOP_1, \ldots, IOP_n)$$

Central value resistant to extreme outliers from corneal irregularities. Best for skewed distributions where corneal biomechanical responses produce asymmetric measurement patterns.

**Clinical IOP (Range Midpoint):**
$$IOP_{clinical} = \frac{IOP_{min} + IOP_{max}}{2}$$

Represents functional pressure range center. Useful for assessing total pressure fluctuation span across measurement sessions, particularly relevant for diurnal variation assessment.

**Mean IOP (Arithmetic Average):**
$$IOP_{mean} = \frac{1}{n}\sum_{i=1}^{n} IOP_i$$

Standard average, sensitive to all outliers. Use only when measurement consistency is very high (variability < 2 mmHg), indicating stable corneal properties across sessions.

---

## DISCLAIMER

> [!WARNING]  
> **NOT a medical device. NOT for diagnosis.**
> This software is built only and restricted to research porpuses. Despite it's based on mathematical and statistical evidence and methods, it has not been clinically validated nor approved by any health authority. It should NOT be used for medical diagnosis, treatment decisions, or clinical management of patients. **Use it just as a monitoring tool**.

---

## Author
https://edujbarrios.com - https://github.com/edujbarrios

> [!WARNING]  
> **The author is not responsible for any misuse or misinterpretation of the results provided by this software. Always consult a qualified professional for medical advice and decisions.**
---

*For any required updates or issues, please open an issue or pull request. Alternatively, contact me trough my email.*

## Work in Progress
> [!NOTE]  
> This project is still work in progress. New features and improvements will be added over time. Incluiding:
> - User management and data storage for long term monitoring.
> - .exe or standalone app distribution for easy use without Python setup.
> - Research new formulas and methods for IOP estimation.

## Citing
if you find this project useful, consider starring the repository on GitHub to support its development!

Also if you used it in any research work, please cite it as:


```bibtex
@misc{barrios2025realiop,
  author       = {Barrios, Eduardo J.},
  title        = {real-iop-estimator},
  year         = {2026},
  howpublished = {\url{https://github.com/edujbarrios/real-iop-estimator}},
  note         = {GitHub repository}
}
```


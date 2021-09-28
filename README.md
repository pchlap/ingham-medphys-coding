# Ingham Medical Physics Coding Challenge

## Welcome

Welcome to the Ingham/UNSW Medical Physics Coding Challenge for September/October 2021. Thank you for your interest in joining our team. Before we progress with the hiring process, we'd like to ask you to complete this challenge. This is a chance for you to showcase your skills to us, there is no correct or incorrect solution to this challenge.

## Task

We've included some data for approximately 200 patients treated for Head and Neck Cancer extracted from the publicly available [HNSCC dataset](https://wiki.cancerimagingarchive.net/display/Public/HNSCC). This is a comprehensive dataset with a number of different attributes typically tracked for patients receiving cancer treatment.

Your task is to implement a web-based dashboard/GUI which can visualise some of this data. It's up to you what you would like to display and what kind of functionality you want to provide to a user to explore the data. You may also use the programming language of your choice and any libraries/frameworks you like. See below for a few tips in case you need some help getting started.

> Important: The are many different attributes in the dataset, we do not expect your dashboard to deal with and visualise all of them. Pick out some key attributes which you think would be most interesting to display.

## Submission

Since we commonly use GitHub for collaborating on open source code, ideally you will fork this repository and add your code directly in there. Best to follow up with a GitHub Pull Request back into our repo so we can see your code. This would require making your submission public, if you would prefer to keep your code private, please add it to a private GitHub repository and add @pchlap with read permissions.

In addition, it would be great if you can make your dashboard really easy to run/access. Think about how you might best package your tool and include some instructions in your submission on how to run your dashboard.

> Please submit by 10am on Tuesday 5th October 2021.

## Tips

Here are a few tips to help you get started with the challenge:

1. Python is commonly used in research thanks to its ease of use. [Dash](https://dash.plotly.com/) is one of many Python libraries which can be used to easily create web-based dashboards.

2. See `challenge_september_2021.py` for some code on getting started using Python and Dash. Use the following commands in your Python environment to run the example:

```bash
pip install -r requirements.txt
python challenge_september_2021.py
```

3. At diagnosis, the patient's disease is assigned a stage (I, II, III, IVA, IVB). Typically one can expect poorer overall survival the higher the stage at diagnosis. A good starting point for the dashboard could be to visualise the overall survival based on the stage. Additionally you could allow the user to filter by gender or an age bracket.

4. Web applications are often deployed using Docker. Perhaps you might like to build or even deploy ([Heroku](https://www.heroku.com/) has a free plan) a Docker image which runs your dashboard.

## Data

You can find the clinical data for this challenge in the `data/hnscc.csv` file.

This data was extracted from the HNSCC dataset: https://wiki.cancerimagingarchive.net/display/Public/HNSCC:
- Grossberg A, Elhalawani H, Mohamed A, Mulder S, Williams B, White AL, Zafereo J, Wong AJ, Berends JE, AboHashem S, Aymard JM, Kanwar A, Perni S, Rock CD, Chamchod S, Kantor M, Browne T, Hutcheson K, Gunn GB, Frank SJ, Rosenthal DI, Garden AS, Fuller CD, M.D. Anderson Cancer Center Head and Neck Quantitative Imaging Working Group. (2020) HNSCC [ Dataset ]. The Cancer Imaging Archive. DOI: https://doi.org/10.7937/k9/tcia.2020.a8sh-7363

- Grossberg  A, Mohamed A, Elhalawani H, Bennett W, Smith K, Nolan T,  Williams B, Chamchod S, Heukelom J, Kantor M, Browne T, Hutcheson K, Gunn G, Garden A, Morrison W, Frank S, R osenthal D, Freymann J, Fuller C. (2018) Imaging and Clinical Data Archive for Head and Neck Squamous Cell Carcinoma Patients Treated with Radiotherapy. Scientific Data 5 :180173 (2018) DOI: 10.1038/sdata.2018.173

- Elhalawani, H., Mohamed, A., White, A. et al. Matched computed tomography segmentation and demographic data for oropharyngeal cancer radiomics challenges. Sci Data 4, 170077 (2017). DOI: 10.1038/sdata.2017.77
TCIA Citation

- Clark K, Vendt B, Smith K, Freymann J, Kirby J, Koppel P, Moore S, Phillips S, Maffitt D, Pringle M, Tarbox L, Prior F. The Cancer Imaging Archive (TCIA): Maintaining and Operating a Public Information Repository, Journal of Digital Imaging, Volume 26, Number 6, December, 2013, pp 1045-1057. DOI: 10.1007/s10278-013-9622-7

## Good luck

Thanks for participating, we look forward to you submission! If you have any questions please contact:  **Phillip Chlap**: [phillip.chlap@unsw.edu.au](phillip.chlap@unsw.edu.au).

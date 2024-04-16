# LinkedIn Job Posting Filter Chrome Extension

Generative AI is transforming user interaction by enabling personalized experiences and conversational interfaces. Ever thought about having a Chrome extension that filters job postings for you on LinkedIn? Well, that's exactly what this project aims to do!

## Overview

This project leverages Flask for the backend running on CodeSandbox and GPT-3.5 for entity extraction. It's a quick demo of v1, which was developed within a few hours. The goal is to create a seamless experience for users actively searching for jobs on LinkedIn.

## Features

- **Entity Extraction**: Utilizing GPT-3.5 for entity extraction, the system can interpret natural language queries to filter job postings effectively.
- **Real-time Filtering**: Users can specify various parameters such as job title, location, time period, experience level, and salary to filter job postings in real-time.
- **Supported Queries**:
  - Show me Database Administrator job postings in SF CA within the past 15 minutes (supports seconds as well)
  - Software developer job postings in NY posted over the past one month.
  - Show me software developer job posting in NY hiring for associate which pays over 100K USD
  - SPM in San Francisco Bay Area with pay over 120k (interprets SPM as Senior Product Manager)

## Future Enhancements

In upcoming releases, additional filters will be integrated, along with an option to filter job postings based on the user's resume. Here are some potential enhancements that might be fun to add:

- **Advanced Filters**: Integrate more filters such as company size, industry, required skills, etc., to provide users with more refined search results.
- **Resume Integration**: Allow users to upload their resumes, and the system can filter job postings based on their skills and experience.
- **User Interface Improvements**: Enhance the user interface of the Chrome extension to provide a more intuitive and seamless experience.
- **Multi-platform Support**: Extend the functionality to support other job platforms besides LinkedIn, providing users with a broader range of options.


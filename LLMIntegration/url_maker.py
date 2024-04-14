from urllib.parse import urlencode, urlparse, parse_qs


class LinkedInURLRecreator:
    def __init__(self, base_url):
        self.base_url = base_url
        self.parsed_url = urlparse(base_url)
        self.query_params = parse_qs(self.parsed_url.query)

    def recreate_url(self, new_params):
        # Extracting currentJobId and origin
        current_job_id = self.query_params.get('currentJobId', [''])[0]
        origin = self.query_params.get('origin', [''])[0]

        # Update query parameters with new_params
        self.query_params.update(new_params)
        self.query_params['currentJobId'] = [current_job_id]
        self.query_params['origin'] = [origin]
        # remove  time_period from query params
        time = None
        if 'time_period' in self.query_params:
            time = self.query_params.pop('time_period')
        if time:
            self.query_params['time_period'] = "f_TPR=r" + str(time)
        # Reconstruct query string
        new_query_string = urlencode(self.query_params, doseq=True)

        # Reconstruct final URL
        new_url = f"{self.parsed_url.scheme}://{self.parsed_url.netloc}{self.parsed_url.path}?{new_query_string}"

        return new_url




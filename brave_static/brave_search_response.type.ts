export interface BraveSearchResponse {
  query: Query;
  mixed: Mixed;
  type: string;
  videos: Videos;
  web: Web;
}

interface Web {
  type: string;
  results: Result2[];
  family_friendly: boolean;
}

interface Result2 {
  title: string;
  url: string;
  is_source_local: boolean;
  is_source_both: boolean;
  description: string;
  profile: Profile;
  language: string;
  family_friendly: boolean;
  type: string;
  subtype: string;
  meta_url: Metaurl;
  extra_snippets?: string[];
  page_age?: string;
  thumbnail?: Thumbnail2;
  age?: string;
  qa?: Qa;
  article?: Article;
  deep_results?: Deepresults;
  video?: Video2;
}

interface Video2 {
  duration: string;
  views: string;
  thumbnail: Thumbnail3;
}

interface Deepresults {
  buttons: Button[];
}

interface Button {
  type: string;
  title: string;
  url: string;
}

interface Article {
  author: Author[];
  date: string;
  publisher: Publisher;
}

interface Publisher {
  type: string;
  name: string;
  thumbnail: Thumbnail3;
  url?: string;
}

interface Thumbnail3 {
  src: string;
  original: string;
}

interface Author {
  type: string;
  name: string;
  url?: string;
}

interface Qa {
  question: string;
  answer: Answer;
}

interface Answer {
  text: string;
  upvoteCount: number;
}

interface Thumbnail2 {
  src: string;
  original: string;
  logo: boolean;
}

interface Profile {
  name: string;
  url: string;
  long_name: string;
  img: string;
}

interface Videos {
  type: string;
  results: Result[];
  mutated_by_goggles: boolean;
}

interface Result {
  type: string;
  url: string;
  title: string;
  description: string;
  age: string;
  page_age: string;
  video: Video;
  meta_url: Metaurl;
  thumbnail: Thumbnail;
}

interface Thumbnail {
  src: string;
}

interface Metaurl {
  scheme: string;
  netloc: string;
  hostname: string;
  favicon: string;
  path: string;
}

interface Video {
}

interface Mixed {
  type: string;
  main: Main[];
  top: Top[];
  side: any[];
}

interface Top {
  type: string;
  index: number;
  all: boolean;
}

interface Main {
  type: string;
  index?: number;
  all: boolean;
}

interface Query {
  original: string;
  show_strict_warning: boolean;
  is_navigational: boolean;
  is_news_breaking: boolean;
  spellcheck_off: boolean;
  country: string;
  bad_results: boolean;
  should_fallback: boolean;
  postal_code: string;
  city: string;
  header_country: string;
  more_results_available: boolean;
  state: string;
  summary_key: string;
}
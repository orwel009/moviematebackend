from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import AdminMovie

SAMPLE = [
    {"title":"Winter's Edge","media_type":"movie","director":"C. Morgan","genre":"Thriller","platform":"Netflix","total_episodes":None},
    {"title":"Shadow District","media_type":"tv","director":"R. Ahmed","genre":"Crime","platform":"Prime","total_episodes":8},
    {"title":"Glass Horizon","media_type":"movie","director":"L. Barrett","genre":"Sci-Fi","platform":"HBO","total_episodes":None},
    {"title":"Hidden Springs","media_type":"tv","director":"D. Kwan","genre":"Drama","platform":"Hulu","total_episodes":10},
    {"title":"City of Emberfall","media_type":"movie","director":"T. Lin","genre":"Fantasy","platform":"Disney+","total_episodes":None},
    {"title":"Neptune Rising","media_type":"tv","director":"S. Cho","genre":"Sci-Fi","platform":"Netflix","total_episodes":7},
    {"title":"Deepwater Code","media_type":"movie","director":"M. Collins","genre":"Action","platform":"Prime","total_episodes":None},
    {"title":"Harbor Lights","media_type":"tv","director":"O. Tanaka","genre":"Romance","platform":"Disney+","total_episodes":6},
    {"title":"Iron Veil","media_type":"movie","director":"P. Grant","genre":"Mystery","platform":"HBO","total_episodes":None},
    {"title":"Emerald Path","media_type":"tv","director":"G. Alvarez","genre":"Adventure","platform":"Netflix","total_episodes":9},

    {"title":"Nocturne Avenue","media_type":"movie","director":"W. Russo","genre":"Drama","platform":"Prime","total_episodes":None},
    {"title":"Saffron Fields","media_type":"tv","director":"A. Batra","genre":"Historical","platform":"Hulu","total_episodes":12},
    {"title":"Broken Compass","media_type":"movie","director":"E. Hwang","genre":"Adventure","platform":"IndieStream","total_episodes":None},
    {"title":"The Blue Port","media_type":"tv","director":"K. Silva","genre":"Documentary","platform":"Curiosity","total_episodes":5},
    {"title":"Silent Rivers","media_type":"movie","director":"R. Kumar","genre":"Romance","platform":"Netflix","total_episodes":None},
    {"title":"Nightshift Protocol","media_type":"tv","director":"V. Ortega","genre":"Sci-Fi","platform":"Prime","total_episodes":8},
    {"title":"Opal Skies","media_type":"movie","director":"J. Dimitrov","genre":"Drama","platform":"HBO","total_episodes":None},
    {"title":"Whispering Pines","media_type":"tv","director":"S. Mishra","genre":"Thriller","platform":"Hulu","total_episodes":10},
    {"title":"Crimson Harbor","media_type":"movie","director":"Y. Nakamoto","genre":"Crime","platform":"Prime","total_episodes":None},
    {"title":"Voyager Station","media_type":"tv","director":"B. Kovacs","genre":"Sci-Fi","platform":"Netflix","total_episodes":11},

    {"title":"Saltwind Tales","media_type":"movie","director":"H. Schneider","genre":"Adventure","platform":"Disney+","total_episodes":None},
    {"title":"Greyhall Academy","media_type":"tv","director":"C. Das","genre":"Fantasy","platform":"HBO","total_episodes":9},
    {"title":"Twinline","media_type":"movie","director":"M. Foster","genre":"Thriller","platform":"Prime","total_episodes":None},
    {"title":"Golden Ashes","media_type":"tv","director":"A. Noor","genre":"Drama","platform":"Hulu","total_episodes":7},
    {"title":"Shoreline Echo","media_type":"movie","director":"J. Mathews","genre":"Drama","platform":"Netflix","total_episodes":None},
    {"title":"Verdant Frontier","media_type":"tv","director":"K. Raman","genre":"Adventure","platform":"Prime","total_episodes":8},
    {"title":"The Last Timberwolf","media_type":"movie","director":"G. Novak","genre":"Nature","platform":"Curiosity","total_episodes":None},
    {"title":"Radiant Sector","media_type":"tv","director":"L. Sparrow","genre":"Sci-Fi","platform":"HBO","total_episodes":10},
    {"title":"Silent Aurora","media_type":"movie","director":"F. Rivera","genre":"Fantasy","platform":"Disney+","total_episodes":None},
    {"title":"Cloudpiercer","media_type":"tv","director":"Y. Arora","genre":"Documentary","platform":"Curiosity","total_episodes":4},

    {"title":"Mariner's Call","media_type":"movie","director":"A. Castillo","genre":"Adventure","platform":"Prime","total_episodes":None},
    {"title":"Scarlet Horizon","media_type":"tv","director":"M. Takahashi","genre":"Drama","platform":"Netflix","total_episodes":8},
    {"title":"The Vault Runner","media_type":"movie","director":"E. Sokolov","genre":"Thriller","platform":"HBO","total_episodes":None},
    {"title":"Fractured Earth","media_type":"tv","director":"J. Martins","genre":"Sci-Fi","platform":"Disney+","total_episodes":10},
    {"title":"Wildshore Harbor","media_type":"movie","director":"H. Bhat","genre":"Romance","platform":"Netflix","total_episodes":None},
    {"title":"Ironfall Legion","media_type":"tv","director":"T. Johansson","genre":"Action","platform":"Prime","total_episodes":12},
    {"title":"Sparrowtail","media_type":"movie","director":"C. Mendes","genre":"Drama","platform":"Hulu","total_episodes":None},
    {"title":"Ghostline District","media_type":"tv","director":"U. Fernandes","genre":"Thriller","platform":"HBO","total_episodes":6},
    {"title":"Autumn Skye","media_type":"movie","director":"D. Chan","genre":"Indie","platform":"IndieStream","total_episodes":None},
    {"title":"Starcrest Chronicles","media_type":"tv","director":"P. Grayson","genre":"Sci-Fi","platform":"Netflix","total_episodes":9},

    {"title":"Crimson Yard","media_type":"movie","director":"R. Malik","genre":"Mystery","platform":"Prime","total_episodes":None},
    {"title":"Hollowgate","media_type":"tv","director":"K. Dupont","genre":"Horror","platform":"Shudder","total_episodes":10},
    {"title":"Glass Orchard","media_type":"movie","director":"S. Patel","genre":"Romance","platform":"Disney+","total_episodes":None},
    {"title":"Mesa Frontier","media_type":"tv","director":"O. Mendes","genre":"Adventure","platform":"Netflix","total_episodes":7},
    {"title":"Sunset Paragraphs","media_type":"movie","director":"I. Moreno","genre":"Drama","platform":"Prime","total_episodes":None},
    {"title":"Voltronic Edge","media_type":"tv","director":"L. Carter","genre":"Sci-Fi","platform":"HBO","total_episodes":11},
    {"title":"Fogtown Memoirs","media_type":"movie","director":"A. Silva","genre":"Mystery","platform":"Netflix","total_episodes":None},
    {"title":"Nimbus Station","media_type":"tv","director":"T. Yamamoto","genre":"Sci-Fi","platform":"Hulu","total_episodes":9},
    {"title":"Orchid Valley","media_type":"movie","director":"V. Arora","genre":"Drama","platform":"IndieStream","total_episodes":None},
    {"title":"The Meridian Files","media_type":"tv","director":"C. Leblanc","genre":"Crime","platform":"Prime","total_episodes":8},

    {"title":"Shattered Reef","media_type":"movie","director":"G. Navarro","genre":"Thriller","platform":"Prime","total_episodes":None},
    {"title":"The Whisper Vault","media_type":"tv","director":"Z. Park","genre":"Mystery","platform":"Netflix","total_episodes":10},
    {"title":"Oceansong","media_type":"movie","director":"B. Holtz","genre":"Documentary","platform":"Curiosity","total_episodes":None},
    {"title":"The Golden Corridor","media_type":"tv","director":"F. Rubio","genre":"Drama","platform":"HBO","total_episodes":6},
    {"title":"Copper Ridge","media_type":"movie","director":"C. Nair","genre":"Adventure","platform":"Disney+","total_episodes":None},
    {"title":"Quiet District","media_type":"tv","director":"E. Laurent","genre":"Romance","platform":"Hulu","total_episodes":7},
    {"title":"Shadow Orchard","media_type":"movie","director":"P. Ivanov","genre":"Mystery","platform":"Prime","total_episodes":None},
    {"title":"Gravity Pulse","media_type":"tv","director":"R. Sethi","genre":"Sci-Fi","platform":"Netflix","total_episodes":12},
    {"title":"Bluewood Dreams","media_type":"movie","director":"H. Jensen","genre":"Family","platform":"Netflix","total_episodes":None},
    {"title":"Empire of Dunes","media_type":"tv","director":"T. Romero","genre":"Adventure","platform":"Prime","total_episodes":10},

    {"title":"Winterline","media_type":"movie","director":"J. Okada","genre":"Drama","platform":"Hulu","total_episodes":None},
    {"title":"Cobalt Verse","media_type":"tv","director":"L. Dimitri","genre":"Sci-Fi","platform":"HBO","total_episodes":8},
    {"title":"Burnished Hearts","media_type":"movie","director":"N. Sterling","genre":"Romance","platform":"Netflix","total_episodes":None},
    {"title":"City Under Neon","media_type":"tv","director":"V. Zhang","genre":"Crime","platform":"Prime","total_episodes":9},
    {"title":"Serenity Ashes","media_type":"movie","director":"A. García","genre":"Historical","platform":"Disney+","total_episodes":None},
    {"title":"Lonewatch Beacon","media_type":"tv","director":"H. Fischer","genre":"Thriller","platform":"HBO","total_episodes":7},
    {"title":"Misty Riverbend","media_type":"movie","director":"M. Isaac","genre":"Drama","platform":"IndieStream","total_episodes":None},
    {"title":"The Aurora Directive","media_type":"tv","director":"C. Nguyen","genre":"Sci-Fi","platform":"Hulu","total_episodes":10},
    {"title":"Year of the Sparrow","media_type":"movie","director":"S. Kohli","genre":"Adventure","platform":"Prime","total_episodes":None},
    {"title":"Hearts of Ironvale","media_type":"tv","director":"R. Dominguez","genre":"Fantasy","platform":"Netflix","total_episodes":11},
    
    {"title":"The Midnight Runner","media_type":"movie","director":"J. Clark","genre":"Action","platform":"Prime","total_episodes":None},
    {"title":"Starlight Avenue","media_type":"tv","director":"N. Voss","genre":"Drama","platform":"Netflix","total_episodes":8},
    {"title":"Echoes of Tomorrow","media_type":"movie","director":"M. Patel","genre":"Sci-Fi","platform":"HBO","total_episodes":None},
    {"title":"Baker Street Mysteries","media_type":"tv","director":"L. Greene","genre":"Mystery","platform":"Prime","total_episodes":10},
    {"title":"Solace","media_type":"movie","director":"A. Roy","genre":"Romance","platform":"Netflix","total_episodes":None},
    {"title":"Kingdoms & Crowns","media_type":"tv","director":"H. Kim","genre":"Fantasy","platform":"Disney+","total_episodes":12},
    {"title":"Rust & Rain","media_type":"movie","director":"F. Silva","genre":"Drama","platform":"Prime","total_episodes":None},
    {"title":"Neon Nights","media_type":"tv","director":"K. Shah","genre":"Thriller","platform":"Hulu","total_episodes":6},
    {"title":"Harvest Moon","media_type":"movie","director":"D. Rao","genre":"Family","platform":"Netflix","total_episodes":None},
    {"title":"Quantum Fault","media_type":"tv","director":"E. Torres","genre":"Sci-Fi","platform":"HBO","total_episodes":9},
    
    {"title":"Paper Boats","media_type":"movie","director":"S. Mehta","genre":"Indie","platform":"IndieStream","total_episodes":None},
    {"title":"Silver Compass","media_type":"tv","director":"R. Jain","genre":"Adventure","platform":"Prime","total_episodes":7},
    {"title":"Afterglow","media_type":"movie","director":"T. Alvarez","genre":"Romance","platform":"Netflix","total_episodes":None},
    {"title":"The Last Lantern","media_type":"tv","director":"P. Singh","genre":"Horror","platform":"Shudder","total_episodes":10},
    {"title":"Parallel Lines","media_type":"movie","director":"C. Weber","genre":"Thriller","platform":"HBO","total_episodes":None},
    {"title":"Hidden Archives","media_type":"tv","director":"Y. Nakamura","genre":"Documentary","platform":"Curiosity","total_episodes":5},
    {"title":"Midwinter Road","media_type":"movie","director":"G. Fernandes","genre":"Drama","platform":"Prime","total_episodes":None},
    {"title":"Atlas Rising","media_type":"tv","director":"M. Rossi","genre":"Action","platform":"Netflix","total_episodes":13},
    {"title":"Lanterns in June","media_type":"movie","director":"L. Kumar","genre":"Drama","platform":"IndieStream","total_episodes":None},
    {"title":"Echo Park","media_type":"tv","director":"O. Bennett","genre":"Comedy","platform":"Hulu","total_episodes":8},
    
    {"title":"The Gentle Storm","media_type":"movie","director":"H. Lopez","genre":"Historical","platform":"Prime","total_episodes":None},
    {"title":"Coded Hearts","media_type":"tv","director":"Z. Ali","genre":"Romance","platform":"Disney+","total_episodes":6},
    {"title":"Feral City","media_type":"movie","director":"I. Novak","genre":"Crime","platform":"HBO","total_episodes":None},
    {"title":"Blue Signal","media_type":"tv","director":"K. Müller","genre":"Drama","platform":"Netflix","total_episodes":10},
    {"title":"Paper Lanterns","media_type":"movie","director":"S. Roy","genre":"Indie","platform":"IndieStream","total_episodes":None},
    {"title":"The Long Crossing","media_type":"tv","director":"V. Petrov","genre":"Adventure","platform":"Prime","total_episodes":11},
    {"title":"City of Glass","media_type":"movie","director":"E. Brown","genre":"Mystery","platform":"HBO","total_episodes":None},
    {"title":"The Signal Keeper","media_type":"tv","director":"A. Costa","genre":"Sci-Fi","platform":"Hulu","total_episodes":9},
    {"title":"Quiet Harbor","media_type":"movie","director":"R. Das","genre":"Drama","platform":"Netflix","total_episodes":None},
    {"title":"Northern Lights","media_type":"tv","director":"L. Svensson","genre":"Documentary","platform":"Curiosity","total_episodes":4},
]

class Command(BaseCommand):
    help = "Seed AdminMovie table with sample entries (30)."

    def handle(self, *args, **options):
        created = 0
        for item in SAMPLE:
            title = item['title']
            # skip if exists
            obj, was_created = AdminMovie.objects.get_or_create(
                title=title,
                defaults={
                    'media_type': item.get('media_type', 'movie'),
                    'director': item.get('director'),
                    'genre': item.get('genre'),
                    'platform': item.get('platform'),
                    'total_episodes': item.get('total_episodes'),
                    'synopsis': item.get('synopsis', ''),
                    'poster_url': item.get('poster_url', ''),
                    'created_at': timezone.now(),
                    'updated_at': timezone.now(),
                }
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"AdminMovie seed completed: {created} created, {len(SAMPLE)-created} skipped (already existed)."))
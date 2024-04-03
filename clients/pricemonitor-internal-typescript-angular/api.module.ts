import { NgModule, ModuleWithProviders, SkipSelf, Optional } from '@angular/core';
import { Configuration } from './configuration';
import { HttpClient } from '@angular/common/http';


import { AccountService } from './api/account.service';
import { AmazonIntegrationService } from './api/amazonIntegration.service';
import { CompaniesService } from './api/companies.service';
import { ControlpanelService } from './api/controlpanel.service';
import { DeprecatedService } from './api/deprecated.service';
import { DomainsService } from './api/domains.service';
import { FeedsService } from './api/feeds.service';
import { InternalService } from './api/internal.service';
import { JobsService } from './api/jobs.service';
import { LogsService } from './api/logs.service';
import { LookerService } from './api/looker.service';
import { MonitoringSchedulesService } from './api/monitoringSchedules.service';
import { OffersService } from './api/offers.service';
import { OrdersService } from './api/orders.service';
import { PluginregistrationService } from './api/pluginregistration.service';
import { PreprocessingService } from './api/preprocessing.service';
import { PricerecommendationsService } from './api/pricerecommendations.service';
import { ProductsService } from './api/products.service';
import { ScenariostrategyService } from './api/scenariostrategy.service';
import { SettingsService } from './api/settings.service';
import { StrategyService } from './api/strategy.service';
import { TasksService } from './api/tasks.service';
import { UndocumentedService } from './api/undocumented.service';
import { VendorShopMappingService } from './api/vendorShopMapping.service';

@NgModule({
  imports:      [],
  declarations: [],
  exports:      [],
  providers: []
})
export class ApiModule {
    public static forRoot(configurationFactory: () => Configuration): ModuleWithProviders<ApiModule> {
        return {
            ngModule: ApiModule,
            providers: [ { provide: Configuration, useFactory: configurationFactory } ]
        };
    }

    constructor( @Optional() @SkipSelf() parentModule: ApiModule,
                 @Optional() http: HttpClient) {
        if (parentModule) {
            throw new Error('ApiModule is already loaded. Import in your base AppModule only.');
        }
        if (!http) {
            throw new Error('You need to import the HttpClientModule in your AppModule! \n' +
            'See also https://github.com/angular/angular/issues/20575');
        }
    }
}
